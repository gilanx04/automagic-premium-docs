---
title: "Action - Init Variables Gleeo Project Structure"
source: https://automagic4android.com/action_init_variables_gleeo_project_structure_en.html
archived: 2022-10-01
archive_url: https://web.archive.org/web/20221001212217/https://automagic4android.com/action_init_variables_gleeo_project_structure_en.html
category: action
---

# Action - Init Variables Gleeo Project Structure

The action **Init Variables Gleeo Project Structure** initializes a variable with the domains, projects or tasks from *Gleeo Time Tracker*.

Examples:

- Load all Tasks of a project to show a selection list in Automagic.

### Settings

#### Type

Whether to query the domains, projects or tasks.

#### Variable for Domains

The name of the variable for the domains. [Variables are supported.](action_script.md#string-inline-expressions)

#### Variable for Projects

The name of the variable for the projects. [Variables are supported.](action_script.md#string-inline-expressions)

#### All or Domain specific

Whether to query all projects or just the projects of one particular domain. [Variables are supported.](action_script.md#string-inline-expressions)

#### Domain

The name of the domain to query. [Variables are supported.](action_script.md#string-inline-expressions)

#### Variable for Tasks

The name of the variable for the tasks. [Variables are supported.](action_script.md#string-inline-expressions)

#### All or Project specific

Whether to query all tasks or just the tasks of one particular project. [Variables are supported.](action_script.md#string-inline-expressions)

#### Project

The name of the project to query. [Variables are supported.](action_script.md#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `domains` — the list of domains
- `projects` — the list of projects
- `tasks` — the list of tasks

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
