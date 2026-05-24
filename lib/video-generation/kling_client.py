#!/usr/bin/env python3
"""
Kling 3.0 Image-to-Video API Client

Authentication: JWT (HS256) with Access Key + Secret Key
API Base: https://api.klingai.com
Docs: https://app.klingai.com/global/dev/document-api

Capabilities:
- #1 ELO benchmark score (1243) among all AI video models (Feb 2026)
- Native 4K output up to 60fps, clips up to 15 seconds
- Multi-modal Visual Language (MVL) architecture
- Native multilingual audio + lip-sync (zh, en, es, ja)
- Multi-shot scene logic with character consistency
- Strengths: dance/motion quality, face consistency, dialogue lip-sync
"""

import hmac
import hashlib
import time
import json
import base64
import requests
from pathlib import Path
from typing import Optional


API_BASE = "https://api.klingai.com"

VALID_MODELS = ["kling-v1", "kling-v1-5", "kling-v1-6", "kling-v2-6", "kling-v3"]
VALID_MODES = ["std", "pro", "4k"]
VALID_RATIOS = ["16:9", "9:16", "1:1"]
VALID_DURATIONS = [str(i) for i in range(3, 16)]


def _base64url_encode(data: bytes | str) -> str:
    if isinstance(data, str):
        data = data.encode("utf-8")
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("utf-8")


def create_jwt(access_key: str, secret_key: str) -> str:
    header = _base64url_encode(
        json.dumps({"alg": "HS256", "typ": "JWT"}, separators=(",", ":"))
    )
    payload = _base64url_encode(
        json.dumps(
            {
                "iss": access_key,
                "exp": int(time.time()) + 1800,
                "nbf": int(time.time()) - 5,
            },
            separators=(",", ":"),
        )
    )
    signing_input = f"{header}.{payload}"
    signature = _base64url_encode(
        hmac.new(
            secret_key.encode("utf-8"),
            signing_input.encode("utf-8"),
            hashlib.sha256,
        ).digest()
    )
    return f"{signing_input}.{signature}"


def encode_image(path: str) -> str:
    return base64.b64encode(Path(path).read_bytes()).decode("utf-8")


class KlingClient:
    def __init__(self, access_key: str, secret_key: str):
        self.access_key = access_key
        self.secret_key = secret_key

    def _headers(self) -> dict:
        token = create_jwt(self.access_key, self.secret_key)
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }

    def submit_image_to_video(
        self,
        image_path: str,
        prompt: str,
        *,
        model_name: str = "kling-v3",
        negative_prompt: str = "",
        duration: str = "10",
        aspect_ratio: str = "9:16",
        mode: str = "pro",
        cfg_scale: float = 0.5,
        generate_audio: bool = True,
        callback_url: Optional[str] = None,
    ) -> dict:
        img_b64 = encode_image(image_path)
        payload = {
            "model_name": model_name,
            "image": img_b64,
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "cfg_scale": cfg_scale,
            "mode": mode,
            "duration": duration,
            "aspect_ratio": aspect_ratio,
        }
        if callback_url:
            payload["callback_url"] = callback_url

        resp = requests.post(
            f"{API_BASE}/v1/videos/image2video",
            headers=self._headers(),
            json=payload,
            timeout=120,
        )
        return resp.json()

    def get_task_status(self, task_id: str) -> dict:
        resp = requests.get(
            f"{API_BASE}/v1/videos/image2video/{task_id}",
            headers=self._headers(),
            timeout=30,
        )
        return resp.json()

    def poll_until_done(
        self, task_id: str, max_polls: int = 30, interval: int = 15
    ) -> dict:
        for _ in range(max_polls):
            result = self.get_task_status(task_id)
            status = result.get("data", {}).get("task_status", "unknown")
            if status in ("succeed", "SUCCEEDED", "completed"):
                return result
            if status in ("failed", "FAILED"):
                return result
            time.sleep(interval)
        return {"error": "timeout", "task_id": task_id}
