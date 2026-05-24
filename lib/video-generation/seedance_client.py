#!/usr/bin/env python3
"""
BytePlus Seedance 2.0 Image-to-Video API Client

Authentication: Bearer API Key (obtained from BytePlus ModelArk console)
API Base: https://ark.ap-southeast.bytepluses.com/api/v3
Docs: https://docs.byteplus.com/en/docs/ModelArk/1520757

IMPORTANT: Seedream 2.0 is a text-to-IMAGE model (not video).
           Seedance 2.0 is the VIDEO generation model on BytePlus ModelArk.

Capabilities:
- Native 2K resolution output, 24fps
- Multi-shot storytelling with scene consistency
- Multi-reference image input (up to 9 images)
- Text/image/video/audio multimodal inputs
- Duration: 4-15 seconds
- Aspect ratios: 16:9, 9:16, 4:3, 3:4, 21:9, 1:1, adaptive

Authentication Note:
  BytePlus provides two credential types:
  1. IAM AKSK (Access Key ID + Secret Access Key) - for console/infrastructure APIs
  2. ModelArk API Key - for model inference (Bearer token)

  Content generation REQUIRES a ModelArk API Key (not AKSK).
  To obtain one: BytePlus Console -> ModelArk -> API Keys -> Create API Key
"""

import time
import json
import base64
import requests
from pathlib import Path
from typing import Optional


API_BASE = "https://ark.ap-southeast.bytepluses.com/api/v3"

MODELS = {
    "seedance-2.0": "dreamina-seedance-2-0-260128",
    "seedance-2.0-fast": "dreamina-seedance-2-0-fast-260128",
    "seedance-1.0-lite-i2v": "seedance-1-0-lite-i2v-250428",
    "seedance-1.0-lite-t2v": "seedance-1-0-lite-t2v-250428",
}

VALID_RATIOS = ["16:9", "9:16", "4:3", "3:4", "21:9", "1:1", "adaptive"]
VALID_RESOLUTIONS = ["480p", "720p", "1080p", "2K"]


class SeedanceClient:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def _headers(self) -> dict:
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }

    def submit_image_to_video(
        self,
        image_path: str,
        prompt: str,
        *,
        model: str = "seedance-2.0",
        ratio: str = "9:16",
        resolution: str = "1080p",
        duration: int = 10,
        generate_audio: bool = True,
        watermark: bool = False,
        return_last_frame: bool = False,
        seed: Optional[int] = None,
        callback_url: Optional[str] = None,
    ) -> dict:
        model_id = MODELS.get(model, model)

        img_b64 = base64.b64encode(Path(image_path).read_bytes()).decode("utf-8")

        content = [
            {"type": "text", "text": prompt},
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/png;base64,{img_b64}"},
            },
        ]

        payload = {
            "model": model_id,
            "content": content,
            "ratio": ratio,
            "resolution": resolution,
            "duration": duration,
            "generate_audio": generate_audio,
            "watermark": watermark,
            "return_last_frame": return_last_frame,
        }
        if seed is not None:
            payload["seed"] = seed
        if callback_url:
            payload["callback_url"] = callback_url

        resp = requests.post(
            f"{API_BASE}/contents/generations/tasks",
            headers=self._headers(),
            json=payload,
            timeout=120,
        )
        return resp.json()

    def get_task_status(self, task_id: str) -> dict:
        resp = requests.get(
            f"{API_BASE}/contents/generations/tasks/{task_id}",
            headers=self._headers(),
            timeout=30,
        )
        return resp.json()

    def poll_until_done(
        self, task_id: str, max_polls: int = 30, interval: int = 15
    ) -> dict:
        for _ in range(max_polls):
            result = self.get_task_status(task_id)
            status = result.get("status", "unknown")
            if status == "succeeded":
                return result
            if status in ("failed", "expired", "cancelled"):
                return result
            time.sleep(interval)
        return {"error": "timeout", "task_id": task_id}
