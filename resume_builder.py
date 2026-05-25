#!/usr/bin/env python3
"""MiMo Resume Builder - AI resume creation."""
import os, argparse
from openai import OpenAI

client = OpenAI(api_key=os.getenv("MIMO_API_KEY"), base_url="https://api.xiaomimimo.com/v1")

def build(info, style="modern"):
    r = client.chat.completions.create(model="mimo-v2.5-pro", messages=[
        {"role": "system", "content": f"Create {style} resume in Markdown. ATS-optimized."},
        {"role": "user", "content": info}])
    return r.choices[0].message.content

if __name__ == "__main__":
    p = argparse.ArgumentParser(); p.add_argument("info"); p.add_argument("--style", default="modern"); p.add_argument("-o", default="resume.md")
    a = p.parse_args()
    with open(a.o, "w") as f: f.write(build(a.info, a.style))
    print(f"Saved: {a.o}")
