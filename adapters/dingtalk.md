# 钉钉执行适配器

## 能力检测
- 检查是否有钉钉 MCP（`dingtalk-calendar`）可用；没有则引导用户到钉钉开放平台启用 MCP 并授权日程权限（Calendar.Event.Write / Read）。

## 官方 MCP 工具
- `create_calendar_event`：创建日程
- `list_calendar_events`：查询日程
- `update_calendar_event` / `delete_calendar_event`
- `query_busy_status`：查闲忙（创建前必查）
- `query_available_meeting_room`：查空闲会议室（需要线下会议室时用）

## 创建后回执
日程标题、时间、参会人、是否已发邀请。

## 参考
钉钉官方 MCP 文档：https://open.dingtalk.com/document/development/openclaw-invokes-dingtalk-mcp
创建日程 API：https://open.dingtalk.com/document/development/create-schedule
