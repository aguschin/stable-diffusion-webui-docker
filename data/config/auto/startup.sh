#!/bin/bash
set +x

MODEL_DIR="models/Stable-diffusion"
MODEL_FILE="${MODEL_DIR}/sd_xl_base_1.0.safetensors"
MODEL_URL="https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors"

# Check and download the model checkpoint if it does not exist
apt-get install wget
if [ ! -f "$MODEL_FILE" ]; then
    mkdir -p ${MODEL_DIR}
    wget -O ${MODEL_FILE} ${MODEL_URL}
else
    echo "Model checkpoint exists."
fi

# install controlnet extension
rm -rf extensions/sd-webui-controlnet
git clone https://github.com/Mikubill/sd-webui-controlnet.git extensions/sd-webui-controlnet
pip install --no-cache-dir -r extensions/sd-webui-controlnet/requirements.txt insightface

ADAPTER_DIR="models/ControlNet"
ADAPTER_FILE="${ADAPTER_DIR}/ip-adapter-plus-face_sdxl_vit-h.safetensors"
ADAPTER_URL="https://huggingface.co/h94/IP-Adapter/resolve/main/sdxl_models/ip-adapter-plus-face_sdxl_vit-h.safetensors"

# Download the adapter file if it does not exist
if [ ! -f "$ADAPTER_FILE" ]; then
    mkdir -p ${ADAPTER_DIR}
    wget -O ${ADAPTER_FILE} ${ADAPTER_URL}
else
    echo "Adapter file exists."
fi
