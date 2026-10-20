---
title: "Condition - Execution Count"
source: https://automagic4android.com/condition_execution_count_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: condition
---

# Condition - Execution Count

The condition **Execution Count** checks whether the condition has been executed a certain amount of times. An internal counter is incremented whenever the condition is executed. The counter is reset to zero when the condition is met.

Examples:

- Play an alarm when 2 SMS are received within 5 minutes.
- Turn off the screen when the device is shook 2 times in 10 seconds.

### Settings

#### Count

The count to compare. [Variables are supported.](../actions/action_script.md#string-inline-expressions)

#### Timed

Only consider executions that happened within the given duration.

#### Duration

The maximum age of executions to consider.

---

[← Indeks Condition](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
