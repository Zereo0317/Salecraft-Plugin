#!/usr/bin/env python3
"""
Generate Bali Street Dance Video from Group Photo

Usage:
    # Kling 3.0
    python generate_bali_dance.py --platform kling \
        --access-key YOUR_AK --secret-key YOUR_SK \
        --image /path/to/bali_photo.png

    # BytePlus Seedance 2.0
    python generate_bali_dance.py --platform seedance \
        --api-key YOUR_MODELARK_API_KEY \
        --image /path/to/bali_photo.png

    # Both (parallel)
    python generate_bali_dance.py --platform both \
        --access-key YOUR_AK --secret-key YOUR_SK \
        --api-key YOUR_MODELARK_API_KEY \
        --image /path/to/bali_photo.png
"""

import argparse
import json
import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kling_client import KlingClient
from seedance_client import SeedanceClient
from prompts import (
    KLING_PROMPT,
    KLING_NEGATIVE_PROMPT,
    KLING_PARAMS,
    SEEDANCE_PROMPT,
    SEEDANCE_PARAMS,
)


def run_kling(access_key: str, secret_key: str, image_path: str, poll: bool = False):
    print("=" * 70)
    print("  KLING 3.0 — Bali Street Dance Video Generation")
    print("=" * 70)

    client = KlingClient(access_key, secret_key)

    print(f"\nImage: {image_path}")
    print(f"Model: {KLING_PARAMS['model_name']}")
    print(f"Mode: {KLING_PARAMS['mode']} (1080x1920)")
    print(f"Duration: {KLING_PARAMS['duration']}s")
    print(f"Aspect ratio: {KLING_PARAMS['aspect_ratio']}")
    print(f"Audio: {KLING_PARAMS['generate_audio']}")
    print(f"CFG scale: {KLING_PARAMS['cfg_scale']}")
    print(f"\nPrompt length: {len(KLING_PROMPT)} chars")
    print(f"Submitting...")

    result = client.submit_image_to_video(
        image_path=image_path,
        prompt=KLING_PROMPT,
        model_name=KLING_PARAMS["model_name"],
        negative_prompt=KLING_NEGATIVE_PROMPT,
        duration=KLING_PARAMS["duration"],
        aspect_ratio=KLING_PARAMS["aspect_ratio"],
        mode=KLING_PARAMS["mode"],
        cfg_scale=KLING_PARAMS["cfg_scale"],
    )

    print(f"\nResponse: {json.dumps(result, indent=2, ensure_ascii=False)[:1000]}")

    code = result.get("code", -1)
    if code == 0:
        task_id = result["data"]["task_id"]
        print(f"\nTask submitted: {task_id}")
        if poll:
            print("Polling for completion (this may take 2-5 minutes)...")
            final = client.poll_until_done(task_id)
            print(f"\nFinal: {json.dumps(final, indent=2, ensure_ascii=False)[:2000]}")
        return task_id
    elif code == 1102:
        print("\nAccount balance insufficient. Please top up credits at:")
        print("  https://app.klingai.com/global/dev")
        return None
    else:
        print(f"\nError: code={code}, message={result.get('message')}")
        return None


def run_seedance(api_key: str, image_path: str, poll: bool = False):
    print("=" * 70)
    print("  SEEDANCE 2.0 — Bali Street Dance Video Generation")
    print("=" * 70)

    client = SeedanceClient(api_key)

    print(f"\nImage: {image_path}")
    print(f"Model: {SEEDANCE_PARAMS['model']}")
    print(f"Resolution: {SEEDANCE_PARAMS['resolution']}")
    print(f"Duration: {SEEDANCE_PARAMS['duration']}s")
    print(f"Aspect ratio: {SEEDANCE_PARAMS['ratio']}")
    print(f"Audio: {SEEDANCE_PARAMS['generate_audio']}")
    print(f"\nPrompt length: {len(SEEDANCE_PROMPT)} chars")
    print(f"Submitting...")

    result = client.submit_image_to_video(
        image_path=image_path,
        prompt=SEEDANCE_PROMPT,
        model=SEEDANCE_PARAMS["model"],
        ratio=SEEDANCE_PARAMS["ratio"],
        resolution=SEEDANCE_PARAMS["resolution"],
        duration=SEEDANCE_PARAMS["duration"],
        generate_audio=SEEDANCE_PARAMS["generate_audio"],
        watermark=SEEDANCE_PARAMS["watermark"],
        return_last_frame=SEEDANCE_PARAMS["return_last_frame"],
    )

    print(f"\nResponse: {json.dumps(result, indent=2, ensure_ascii=False)[:1000]}")

    if "id" in result or "task_id" in result:
        task_id = result.get("id") or result.get("task_id")
        print(f"\nTask submitted: {task_id}")
        if poll:
            print("Polling for completion (30-120 seconds typical)...")
            final = client.poll_until_done(task_id)
            print(f"\nFinal: {json.dumps(final, indent=2, ensure_ascii=False)[:2000]}")
        return task_id
    else:
        error = result.get("error", {})
        print(f"\nError: {error.get('code', 'unknown')} — {error.get('message', str(result))}")
        if "AuthenticationError" in str(error):
            print("\nThe ModelArk API requires a Bearer API Key (not AKSK).")
            print("To get one: BytePlus Console -> ModelArk -> API Keys -> Create")
            print("  https://console.byteplus.com")
        return None


def main():
    parser = argparse.ArgumentParser(description="Generate Bali street dance video")
    parser.add_argument("--platform", choices=["kling", "seedance", "both"], default="both")
    parser.add_argument("--image", required=True, help="Path to the Bali group photo")
    parser.add_argument("--access-key", help="Kling Access Key")
    parser.add_argument("--secret-key", help="Kling Secret Key")
    parser.add_argument("--api-key", help="BytePlus ModelArk API Key")
    parser.add_argument("--poll", action="store_true", help="Poll until completion")
    args = parser.parse_args()

    ak = args.access_key or os.environ.get("KLING_ACCESS_KEY")
    sk = args.secret_key or os.environ.get("KLING_SECRET_KEY")
    api_key = args.api_key or os.environ.get("ARK_API_KEY")

    if args.platform in ("kling", "both") and ak and sk:
        run_kling(ak, sk, args.image, args.poll)

    if args.platform in ("seedance", "both") and api_key:
        run_seedance(api_key, args.image, args.poll)

    if args.platform == "kling" and (not ak or not sk):
        print("Error: --access-key and --secret-key required for Kling")
    if args.platform == "seedance" and not api_key:
        print("Error: --api-key required for Seedance")


if __name__ == "__main__":
    main()
