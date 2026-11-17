#!/usr/bin/env bash
# PreToolUse guard: deny Write/Edit/NotebookEdit outside the project directory.
# Fails closed: if the path cannot be determined, the call is denied.
root="$(realpath -m "${CLAUDE_PROJECT_DIR:-$(pwd)}")"
input="$(cat)"
file="$(printf '%s' "$input" | jq -r '.tool_input.file_path // .tool_input.notebook_path // empty' 2>/dev/null)"
deny() {
  jq -n --arg r "$1" '{hookSpecificOutput:{hookEventName:"PreToolUse",permissionDecision:"deny",permissionDecisionReason:$r}}'
  exit 0
}
[ -n "$file" ] || deny "Audit guard: could not determine target path of the write."
case "$file" in /*) abs="$file" ;; *) abs="$root/$file" ;; esac
abs="$(realpath -m "$abs")"
case "$abs" in
  "$root"|"$root"/*) exit 0 ;;
  *) deny "Audit guard: writes outside the project directory are blocked ($abs)." ;;
esac
