# Demo Test Repository - PR Validation POC

A demonstration repository for testing the **GitHub-native PR validation system**. This project validates that the PR automation agent correctly runs setup commands and unit tests, with GitHub branch protection controlling merge decisions.

## ✅ UT Testing Marker

This section was added as part of a UT system check to verify that README updates can be detected and reviewed through the normal workflow.

Verification timestamp: **Tuesday, Apr 28, 2026, 2:19 PM (UTC+5:30)**

### Additional Test1 Update

This line was added to verify README edits and branch push behavior on `test1`.

## 🎯 Purpose

This repository serves as a **proof-of-concept testing ground** for the PR validation agent. It demonstrates:

- ✅ **Automated PR validation** - GitHub Actions workflow triggers on PR events
- ✅ **Base branch merge in CI** - Latest base branch is merged into PR head before testing
- ✅ **Setup command execution** - Repository setup runs with `uv` isolation
- ✅ **Unit test execution** - Tests run and results determine PR status
- ✅ **GitHub-native merge control** - Branch protection enforces required status checks
- ✅ **Single managed comment** - Bot maintains one PR comment with validation results
- ✅ **Outcome labels** - PRs get labeled based on results (`test-failed`, `needs-tests`, `ready-for-review`, `merge-conflict`)

## 🏗️ Architecture Overview

```
Pull Request Raised
   ↓
GitHub Actions Workflow (.github/workflows/pr-validation.yml)
   ↓
PR Validation Action (karthikbgpillai/POC_PR_AUTOMATION@main)
   ↓
Merge base branch into PR head in CI
   ↓
Run setup commands (uv venv, uv pip install -e .)
   ↓
Run unit tests (uv run pytest)
   ↓
┌─────────────────────────────────────┐
│ If setup/tests fail:                │
│  • Update PR comment with failure   │
│  • Apply test-failed label          │
│  • Set failed commit status         │
│  • GitHub blocks merge              │
└─────────────────────────────────────┘
┌─────────────────────────────────────┐
│ If setup/tests pass:                │
│  • Update PR comment with success   │
│  • Apply ready-for-review label     │
│  • Set success commit status        │
│  • GitHub allows merge (if branch   │
│    protection requirements met)     │
└─────────────────────────────────────┘
```

## 📁 Project Structure

```
demo_test_repo/
├── .github/
│   ├── pr-validation.yml          # Validator configuration
│   └── workflows/
│       └── pr-validation.yml      # GitHub Actions workflow
├── src/
│   ├── __init__.py
│   └── calculator.py              # Simple calculator module
├── tests/
│   └── test_calculator.py         # Unit test suite
├── .gitignore                     # Git ignore rules
├── pyproject.toml                 # Project configuration (uv)
├── uv.lock                        # Locked dependencies
├── run_demo.py                    # Standalone demo script
└── README.md                      # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) package manager

### Local Setup

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment
uv venv

# Install dependencies
uv pip install -e .

# Run demo script
uv run python run_demo.py

# Run tests
uv run pytest -v
```

### Expected Output

**Demo script:**
```
=== Demo Test Repository Runner ===
[1] Running sample calculator operations
add(2, 3) = 5
subtract(10, 4) = 6
divide(12, 3) = 4.0

[2] Demonstrating expected guarded failure
divide(5, 0) raised ValueError as expected: Cannot divide by zero

[3] Demo guidance
- Baseline tests in the base branch should keep passing on PR branches.
- New functions added in a PR should also include new tests.
=== Demo complete ===
```

**Test results:**
```
tests/test_calculator.py::test_add PASSED                    [ 25%]
tests/test_calculator.py::test_subtract PASSED               [ 50%]
tests/test_calculator.py::test_divide PASSED                 [ 75%]
tests/test_calculator.py::test_divide_by_zero PASSED         [100%]
============================== 4 passed in 0.01s ===============================
```

## 🧪 Testing PR Validation Scenarios

### Scenario 1: ✅ Passing Baseline Change

**Goal:** Verify that safe changes pass validation.

1. Create a branch from `main`
2. Make a safe refactor (e.g., improve docstrings, add comments)
3. Open a PR
4. **Expected result:**
   - ✅ Base branch merges successfully in CI
   - ✅ Setup commands succeed
   - ✅ All tests pass
   - ✅ PR gets `ready-for-review` label
   - ✅ Commit status is green
   - ✅ Merge button is enabled (if branch protection allows)

### Scenario 2: ❌ Failing Baseline Test

**Goal:** Prove that test failures block merge.

1. Create a branch from `main`
2. Break existing functionality (e.g., change `add()` to return `a + b + 1`)
3. Don't modify tests
4. Open a PR
5. **Expected result:**
   - ✅ Base branch merges successfully in CI
   - ✅ Setup commands succeed
   - ❌ `test_add()` fails
   - ❌ PR gets `test-failed` label
   - ❌ Commit status is red
   - ❌ Merge button is blocked
   - 💬 PR comment shows failure details with log excerpt

### Scenario 3: ⚠️ New Function Without Tests

**Goal:** Prove that new functions require tests.

1. Create a branch from `main`
2. Add a new function (e.g., `multiply()` in `src/calculator.py`)
3. Don't add tests for it
4. Open a PR
5. **Expected result:**
   - ✅ Base branch merges successfully in CI
   - ✅ Setup commands succeed
   - ⚠️ Existing tests pass but coverage analysis detects missing tests
   - ❌ PR gets `needs-tests` label
   - ❌ Commit status is red
   - ❌ Merge button is blocked
   - 💬 PR comment suggests adding tests

### Scenario 4: ✅ New Function With Tests

**Goal:** Prove that properly tested features pass.

1. Create a branch from `main`
2. Add a new function (e.g., `multiply()` in `src/calculator.py`)
3. Add matching test in `tests/test_calculator.py`
4. Open a PR
5. **Expected result:**
   - ✅ Base branch merges successfully in CI
   - ✅ Setup commands succeed
   - ✅ All tests pass (baseline + new)
   - ✅ PR gets `ready-for-review` label
   - ✅ Commit status is green
   - ✅ Merge button is enabled

### Scenario 5: 🔀 Merge Conflict

**Goal:** Verify merge conflict detection in CI.

1. Create two branches from the same base
2. Modify the same line differently in both
3. Merge one branch first
4. Open PR from the second branch
5. **Expected result:**
   - ❌ Base branch merge fails in CI
   - ❌ PR gets `merge-conflict` label
   - ❌ Commit status is red
   - ❌ Merge button is blocked
   - 💬 PR comment explains the conflict and suggests rebasing

## 🔧 Configuration

### PR Validation Config (`.github/pr-validation.yml`)

```yaml
version: 1

status:
  context: "intelligent-pr-validation"

setup:
  commands:
    - "uv venv"              # Create isolated environment
    - "uv pip install -e ."  # Install project with dependencies

tests:
  command: "uv run pytest -q --maxfail=1"  # Run tests with uv

test_detection:
  test_file_patterns:
    - "tests/**"
    - "**/test_*.py"
  require_symbol_reference: true
  allow_llm_coverage_review: true

labels:
  enabled: true
  test_failed: "test-failed"
  needs_tests: "needs-tests"
  ready_for_review: "ready-for-review"
  merge_conflict: "merge-conflict"

auto_merge:
  enabled: false
```

### GitHub Actions Workflow (`.github/workflows/pr-validation.yml`)

```yaml
name: PR Validation Demo

on:
  pull_request:
    types: [opened, synchronize, reopened, ready_for_review]

permissions:
  contents: read
  pull-requests: write
  issues: write
  statuses: write

jobs:
  validate-pr:
    runs-on: ubuntu-latest
    steps:
      - uses: karthikbgpillai/POC_PR_AUTOMATION@main
        with:
          config-path: .github/pr-validation.yml
          langgraph-url: ${{ secrets.LANGGRAPH_SERVICE_URL }}
          python-version: "3.11"
          uv-version: "0.4.27"
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          LANGGRAPH_SERVICE_TOKEN: ${{ secrets.LANGGRAPH_SERVICE_TOKEN }}
```

## 🔐 Security & Setup

### Required GitHub Secrets

Add these secrets to your repository settings:

1. **`LANGGRAPH_SERVICE_URL`** - Your LangGraph service endpoint (optional for analysis)
2. **`LANGGRAPH_SERVICE_TOKEN`** - Authentication token for LangGraph (optional)
3. **`GITHUB_TOKEN`** - Automatically provided by GitHub Actions

⚠️ **Never commit these values to the repository!**

### Branch Protection (Required)

To enforce validation:

1. Go to **Settings** → **Branches**
2. Add protection rule for `main`
3. Enable:
   - ✅ **Require status checks to pass before merging**
   - ✅ **Require `intelligent-pr-validation` status check**
   - ✅ Require branches to be up to date before merging
   - ✅ Require linear history (optional)

Once configured:
- ❌ Red check → Merge blocked
- ✅ Green check → Merge allowed

## 🔄 Workflow Execution Order

When a PR is created or updated:

1. **Trigger** - PR opened/synchronized/reopened/ready_for_review
2. **Checkout** - PR head commit is checked out
3. **Merge Base** - Latest base branch merged into PR head in CI
4. **Setup** - `uv venv` + `uv pip install -e .`
5. **Test** - `uv run pytest -q --maxfail=1`
6. **Status Update** - Commit status set to success/failure
7. **Comment** - Single managed PR comment updated
8. **Labels** - Outcome labels applied/removed
9. **Branch Protection** - GitHub enforces merge rules

## 📦 Dependencies

Managed via `uv` for fast, reliable, and reproducible builds:

- **pytest** - Testing framework
- **Python 3.8+** - Runtime

All dependencies are locked in [`uv.lock`](uv.lock) for reproducibility.

## 🎓 What This POC Demonstrates

### GitHub-Native Validation
- No external merge decision logic
- GitHub branch protection controls merge
- Failed checks block merge automatically
- Passed checks enable merge (subject to other rules)

### For Developers
- Automated test validation on every PR
- Clear feedback in PR comments
- GitHub Actions logs for debugging
- Local reproduction with same commands

### For Teams
- Consistent code quality standards
- Reduced manual code review burden
- Faster feedback loops
- Enforceable through branch protection

### For Organizations
- Scalable PR validation across repositories
- Customizable validation rules per repo
- Integration with existing GitHub workflows
- Audit trail in GitHub Actions logs

## 🛠️ Technology Stack

- **Language:** Python 3.11
- **Package Manager:** [uv](https://github.com/astral-sh/uv) (fast, reliable Python package installer)
- **Testing:** pytest
- **CI/CD:** GitHub Actions
- **Validation:** Custom PR automation action
- **Merge Control:** GitHub branch protection (native)

## 📝 Development Commands

```bash
# Run demo
uv run python run_demo.py

# Run tests
uv run pytest -v

# Run tests with coverage
uv run pytest --cov=src --cov-report=html

# Install in development mode
uv pip install -e .

# Sync dependencies from lock file
uv pip sync uv.lock

# Update dependencies
uv pip compile pyproject.toml -o uv.lock
```

## 🤝 Contributing

This is a demo repository for POC testing. To test changes:



## 🔗 Related Resources

- [PR Validation Agent Repository](https://github.ibm.com/karthikbgpillai/POC_PR_AUTOMATION)
- [uv Documentation](https://github.com/astral-sh/uv)
- [pytest Documentation](https://docs.pytest.org/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Branch Protection](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)

---

**Made with ❤️ for GitHub-Native PR Validation POC Testing**