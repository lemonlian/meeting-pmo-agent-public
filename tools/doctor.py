#!/usr/bin/env python3
"""知会·环境自检（新用户第一步）

检测本机有哪些办公平台执行能力，输出小白能看懂的结论与下一步。
用法：python tools/doctor.py
"""
import shutil
import subprocess

PLATFORMS = [
    ("飞书", "lark-cli", "pip 或官方脚本安装 lark-cli，然后扫码登录"),
    ("企业微信", "wecom-cli", "安装企业微信官方 CLI，扫码授权日程与会议权限"),
    ("钉钉", "dingtalk", "到钉钉开放平台启用 MCP，授权日程读写权限"),
]


def check(cmd):
    path = shutil.which(cmd)
    if not path:
        return False, "未安装"
    try:
        r = subprocess.run([cmd, "--version"], capture_output=True, text=True, timeout=8)
        return True, (r.stdout or r.stderr).strip().split("\n")[0][:60]
    except Exception as e:
        return False, f"已安装但无法运行：{e}"


def main():
    print("知会·环境自检\n" + "=" * 40)
    ready = []
    for name, cmd, guide in PLATFORMS:
        ok, info = check(cmd)
        print(f"[{'可用' if ok else '缺失'}] {name}: {info}")
        if ok:
            ready.append(name)
        else:
            print(f"      怎么办：{guide}")
    print("=" * 40)
    if ready:
        print("你可以直接使用：" + "、".join(ready))
    else:
        print("还没有可用平台。告诉我你常用哪个办公软件，我带你装哪一个就行。")


if __name__ == "__main__":
    main()
