# DSG Security Baseline: {{asset.name}}

## TL;DR Brief Summary

> **Purpose:** 
{{#asset.kpmg-purpose}}
> {{.}}
{{/asset.kpmg-purpose}}
>
> **Who:** 
{{#asset.kpmg-who}}
>  {{.}}
{{/asset.kpmg-who}}
>
> **What:** 
{{#asset.kpmg-what}}
> {{.}}
{{/asset.kpmg-what}}
>
> **Why:** 
{{#asset.kpmg-why}}
> {{.}}
{{/asset.kpmg-why}}
>

## Summary

{{#asset.description}}
{{.}}
{{/asset.description}}

## {{asset.name}} Controls

{{#asset.controls}}
### Control Title: {{title}}

| Control ID | Description | Objective |
| -- | -- | -- |
| {{id}} | {{description}} | {{objective}} |

#### Control Implementation Steps

| Steps | Reference |
| ----- | --------- |
{{#implementation.steps}}
| {{step}} | {{reference}} |
{{/implementation.steps}}

#### Control Audit Steps
| Steps |
| ----- |
{{#audit.steps}}
| [{{step}}]({{reference}}) |
{{/audit.steps}}
{{/asset.controls}}

## {{asset.name}} Implementation Steps

| Step |
| ---- |
{{#asset.implementation.steps}}
| [{{step}}]({{reference}})
{{/asset.implementation.steps}}

## {{asset.name}} Audit Steps

| Step |
| ---- |
{{#asset.audit.steps}}
| [{{step}}]({{reference}}) |
{{/asset.audit.steps}}

## References

### KPMG Internal References

{{#asset.references.kpmg-refs}}
- [{{title}}]({{http-url}})
{{/asset.references.kpmg-refs}}

### External References

{{#asset.references.external-refs}}
- [{{title}}]({{http-url}})
{{/asset.references.external-refs}}

