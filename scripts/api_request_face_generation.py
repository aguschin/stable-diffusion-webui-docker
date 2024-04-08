import requests
import base64
import os


payload = {
    "batch_size": 1,
    "cfg_scale": 7,
    "comments": {},
    "denoising_strength": 0.7,
    "disable_extra_networks": False,
    "do_not_save_grid": False,
    "do_not_save_samples": False,
    "enable_hr": False,
    "height": 1024,
    "hr_negative_prompt": "",
    "hr_prompt": "",
    "hr_resize_x": 0,
    "hr_resize_y": 0,
    "hr_scale": 2,
    "hr_second_pass_steps": 0,
    "hr_upscaler": "Latent",
    "n_iter": 1,
    "negative_prompt": "disfigured, ugly, bad, immature, cartoon, anime, 3d, painting, b&w, monochrome, low-res, bad anatomy, worst quality, low quality\n",
    "override_settings": {},
    "override_settings_restore_afterwards": True,
    "prompt": "A close-up portrait of a white man for a passport photo, with a friendly expression, showcasing only his head against a white background. The rest of his body is not visible.",
    "restore_faces": False,
    "s_churn": 0,
    "s_min_uncond": 0,
    "s_noise": 1,
    "s_tmax": None,
    "s_tmin": 0,
    "sampler_name": "DPM++ 2M Karras",
    "script_args": [],
    "script_name": None,
    "seed": -1,
    "seed_enable_extras": True,
    "seed_resize_from_h": -1,
    "seed_resize_from_w": -1,
    "steps": 50,
    "styles": [],
    "subseed": -1,
    "subseed_strength": 0,
    "tiling": False,
    "width": 1024,
}

r = requests.post("http://127.0.0.1:7860/sdapi/v1/txt2img", json=payload)
r.raise_for_status()

os.makedirs("images/faces", exist_ok=True)
with open("images/faces/1.png", "wb") as f:
    f.write(base64.b64decode(r.json()["images"][0]))
