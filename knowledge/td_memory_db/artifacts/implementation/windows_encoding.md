# Windows Environment Compatibility

During local development on Windows, encoding issues can arise when printing Unicode characters (emojis, box-drawing characters) to the console if the default encoding is `cp1252`.

## 1. Global Standard IO Reconfiguration
Explicitly reconfiguring `stdout` and `stderr` to use `utf-8` at the application entry point.

```python
import sys

if sys.platform == 'win32':
    try:
        # Reconfigure to handle emojis and Vietnamese characters in console
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
```

## 2. ASCII Fallbacks
To ensure maximum compatibility across terminals, fallback to ASCII-safe symbols for status indicators:
- Success: `[green]+[/green]` instead of `✓`
- Warning/Error: `[bold red]WARNING[/bold red]` instead of `⚠`
- Inactive: `[yellow]-[/yellow]` instead of `⊘`
