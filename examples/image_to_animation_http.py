import argparse
import base64
from flask import Flask, render_template, request
import json
import os
import sys
import yaml

# Set environment variables for OSMesa before importing any OpenGL related modules
os.environ['PYOPENGL_PLATFORM'] = 'osmesa'
os.environ['DISPLAY'] = ':99'

from image_to_animation import image_to_animation

app = Flask(__name__, template_folder=os.path.abspath("./fixer_app/"))

@app.route("/image_to_animation_http", methods=["POST"])
def image_to_animation_http():
    try:
        data = request.get_json()
        img_fn = data['img_fn']
        char_anno_dir = data['char_anno_dir']
        motion_cfg_fn = data['motion_cfg_fn']
        retarget_cfg_fn = data['retarget_cfg_fn']
        image_to_animation(img_fn, char_anno_dir, motion_cfg_fn, retarget_cfg_fn)
        return {"status": "success", "message": "Animation created successfully"}
    except Exception as e:
        import traceback
        error_msg = f"Error: {str(e)}\nTraceback: {traceback.format_exc()}"
        print(error_msg)
        return {"status": "error", "message": error_msg}, 500

if __name__ == "__main__":
    app.run(port=5061, debug=True)