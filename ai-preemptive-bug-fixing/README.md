# AI: Preemptive Bug Fixing

## Task
Review a vulnerable C function (add_node_end for a singly linked list) using a structured AI prompt. Identify logical errors and memory safety flaws, then generate the corrected code.

## Files
- **vulnerable.c**: Original buggy function with a linking error, missing NULL check, and uninitialized fields in an early return path.
- **corrected.c**: Hand‑fixed version that:
  - Checks `malloc` return value
  - Initializes all fields immediately after allocation
  - Correctly stops traversal at the last node
  - Links the new node using `current->next`

## AI Tool Used
Claude (Anthropic)

## Prompt Summary
Assigned the AI the role of Senior C Developer. Requested analysis of Correctness/Logical Errors (list linking) and Memory/Error Handling (NULL check after malloc). Asked for detailed explanations and the complete corrected function.
