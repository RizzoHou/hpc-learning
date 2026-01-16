# Conventional Commits - Quick Reference

A concise guide to Conventional Commits for daily use.

## Basic Format

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

## Commit Types

| Type | Description | SemVer |
|------|-------------|--------|
| `feat` | New feature | MINOR |
| `fix` | Bug fix | PATCH |
| `docs` | Documentation changes | - |
| `style` | Code style/formatting (no logic change) | - |
| `refactor` | Code restructuring (no feature/fix) | - |
| `perf` | Performance improvements | - |
| `test` | Adding or updating tests | - |
| `build` | Build system or dependencies | - |
| `ci` | CI configuration changes | - |
| `chore` | Maintenance tasks | - |
| `revert` | Revert previous commit | - |

**Note:** Only `feat` and `fix` directly affect SemVer. Other types don't trigger version bumps unless they include breaking changes.

## Breaking Changes

### Using `!` in type/scope
```
feat!: add new API endpoint
feat(api)!: change response format
```

### Using BREAKING CHANGE footer
```
feat: add new configuration option

BREAKING CHANGE: Old config format no longer supported
```

**Both indicate MAJOR version change.**

## Scope (Optional)

Provides context about the affected code area:
- `feat(parser): add array support`
- `fix(auth): resolve token expiration`
- `docs(readme): update installation steps`

## Body (Optional)

Detailed explanation after a blank line:
```
fix: handle null values in user input

Previously, null values caused crashes in the validation
module. Now they're properly handled as empty values.

Additional validation was added to prevent similar issues.
```

## Footers (Optional)

Additional metadata using `token: value` or `token #value` format:
```
feat: add dark mode

Reviewed-by: Jane Doe
Closes: #123
Acked-by: team-lead
```

## Examples

### Simple fix
```
fix: resolve memory leak in cache module
```

### Feature with scope
```
feat(auth): add OAuth2 support
```

### Breaking change with `!`
```
chore!: drop support for Node 12

BREAKING CHANGE: Requires Node 14 or higher
```

### Commit with body and footer
```
fix: prevent race condition in API requests

Added request ID tracking to ensure responses match
the latest request. Removed obsolete timeout logic.

Reviewed-by: Alex Chen
Refs: #456, #789
```

## Quick Rules

1. **Required**: Type, colon, space, description
2. **Optional**: Scope in parentheses, body, footers
3. **Breaking**: Use `!` after type/scope or `BREAKING CHANGE:` footer
4. **Body**: Start with blank line after description
5. **Footers**: Start with blank line after body
6. **Case**: Types are lowercase; `BREAKING CHANGE` is uppercase

## Why Use This?

- **Automatic changelogs** from commit history
- **Semantic versioning** based on commit types
- **Clear communication** of changes to team
- **Structured history** for better project maintenance

---

*Based on the Conventional Commits 1.0.0 specification. For complete details, see the full specification.*