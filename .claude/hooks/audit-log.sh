#!/usr/bin/env bash
# Audit trail: one line per tool call -> .claude/audit/audit.log
# Format: <UTC timestamp> | <event> | <session> | <tool> | <target>
# Never blocks the tool call: any failure here is swallowed.
root="${CLAUDE_PROJECT_DIR:-$(pwd)}"
log="$root/.claude/audit/audit.log"
mkdir -p "$(dirname "$log")" 2>/dev/null
jq -r '
  def target:
    (.tool_input // {}) as $i
    | ($i.file_path // $i.notebook_path // $i.command // $i.pattern // $i.url
       // $i.query // $i.path // $i.description // $i.prompt // "-");
  [ (now | todate),
    (.hook_event_name // "PostToolUse"),
    ((.session_id // "-") | .[0:8]),
    (.tool_name // "-"),
    (target | tostring | gsub("[\r\n\t]+"; " ") | .[0:300]) ]
  | join(" | ")
' >> "$log" 2>/dev/null
exit 0
