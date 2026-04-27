# Demo Test Repository - PR Automation POC

A Python calculator demo project designed to test and validate the **PR Automation POC system**. This repository demonstrates how automated PR validation works with baseline tests, new function detection, and merge conflict handling.

## 🎯 Purpose

This repository serves as a **proof-of-concept testing ground** for the PR automation system. It allows you to verify:

- ✅ **Baseline test validation** - Existing tests from the base branch must pass on PR branches
- ✅ **New function coverage** - Newly added functions require corresponding tests
- ✅ **Merge conflict detection** - CI detects and reports merge conflicts
- ✅ **Automated PR status checks** - GitHub status checks control merge availability
- ✅ **Intelligent labeling** - PRs get labeled based on validation results (`test-failed`, `needs-tests`, `ready-for-review`)

## 🏗️ Project Structure

```
demo_test_repo/
├── .github/
│   ├── pr-validation.yml          # PR validation configuration
│   └── workflows/
│       └── pr-validation.yml      # GitHub Actions workflow
├── src/
│   ├── __init__.py
│   └── calculator.py              # Simple calculator module
├── tests/
│   └── test_calculator.py         # Test suite
├── .gitignore                     # Git ignore rules
├── pyproject.toml                 # Project configuration (uv)
├── uv.lock                        # Locked dependencies for reproducibility
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

## 🧪 Testing PR Automation Scenarios

### Scenario 1: ✅ Passing Baseline Change

**Goal:** Verify that safe changes pass validation.

1. Create a branch from `main`
2. Make a safe refactor (e.g., improve docstrings, add comments)
3. Open a PR
4. **Expected result:**
   - ✅ All tests pass
   - ✅ PR gets `ready-for-review` label
   - ✅ Merge is allowed

### Scenario 2: ❌ Failing Baseline Test

**Goal:** Prove that inherited tests from base branch are enforced.

1. Create a branch from `main`
2. Break existing functionality (e.g., change `add()` to return `a + b + 1`)
3. Don't modify tests
4. Open a PR
5. **Expected result:**
   - ❌ `test_add()` fails
   - ❌ PR gets `test-failed` label
   - ❌ Merge is blocked
   - 💬 PR comment explains the failure

### Scenario 3: ⚠️ New Function Without Tests

**Goal:** Prove that new functions require tests.

1. Create a branch from `main`
2. Add a new function (e.g., `multiply()` in `src/calculator.py`)
3. Don't add tests for it
4. Open a PR
5. **Expected result:**
   - ⚠️ Existing tests may pass
   - ❌ PR fails due to missing test coverage
   - ❌ PR gets `needs-tests` label
   - 💬 PR comment suggests adding tests

### Scenario 4: ✅ New Function With Tests

**Goal:** Prove that properly tested features pass.

1. Create a branch from `main`
2. Add a new function (e.g., `multiply()` in `src/calculator.py`)
3. Add matching test in `tests/test_calculator.py`
4. Open a PR
5. **Expected result:**
   - ✅ All tests pass (baseline + new)
   - ✅ PR gets `ready-for-review` label
   - ✅ Merge is allowed

### Scenario 5: 🔀 Merge Conflict

**Goal:** Verify merge conflict detection.

1. Create two branches from the same base
2. Modify the same line differently in both
3. Merge one branch first
4. Open PR from the second branch
5. **Expected result:**
   - 🔀 CI merge step fails
   - ❌ PR gets `merge-conflict` label
   - ❌ Merge is blocked
   - 💬 PR comment explains the conflict

## 🔧 Configuration

### PR Validation Config (`.github/pr-validation.yml`)

```yaml
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
```

### GitHub Actions Workflow (`.github/workflows/pr-validation.yml`)

```yaml
on:
  pull_request:
    types: [opened, synchronize, reopened, ready_for_review]

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
```

## 🔐 Security & Setup

### Required GitHub Secrets

Add these secrets to your repository settings:

1. **`LANGGRAPH_SERVICE_URL`** - Your LangGraph service endpoint
2. **`LANGGRAPH_SERVICE_TOKEN`** - Authentication token for LangGraph

⚠️ **Never commit these values to the repository!**

### Branch Protection (Recommended)

1. Go to **Settings** → **Branches**
2. Add protection rule for `main`
3. Enable:
   - ✅ Require status checks to pass before merging
   - ✅ Require `intelligent-pr-validation` status check
   - ✅ Require branches to be up to date before merging

## 📦 Dependencies

Managed via `uv` for fast, reliable, and reproducible builds:

- **pytest** - Testing framework
- **Python 3.8+** - Runtime

All dependencies are locked in [`uv.lock`](uv.lock) for reproducibility.

## 🔄 Workflow Execution Order

When a PR is created:

1. **Trigger** - PR opened/synchronized/reopened
2. **Checkout** - Code is checked out
3. **Setup** - `uv venv` + `uv pip install -e .`
4. **Test** - `uv run pytest -q --maxfail=1`
5. **Validation** - LangGraph service analyzes results
6. **Status** - PR status check updated
7. **Labels** - Appropriate labels applied
8. **Comment** - Bot comment added/updated with results

## 🎓 What This POC Demonstrates

### For Developers
- Automated test validation on every PR
- Clear feedback on what needs to be fixed
- Prevents merging broken code
- Encourages test-driven development

### For Teams
- Consistent code quality standards
- Reduced manual code review burden
- Faster feedback loops
- Better collaboration through automation

### For Organizations
- Scalable PR validation across repositories
- Customizable validation rules
- Integration with existing GitHub workflows
- Audit trail of all validation decisions

## 🛠️ Technology Stack

- **Language:** Python 3.11
- **Package Manager:** [uv](https://github.com/astral-sh/uv) (fast, reliable Python package installer)
- **Testing:** pytest
- **CI/CD:** GitHub Actions
- **Validation:** Custom PR automation action
- **AI Analysis:** LangGraph service integration

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

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Open a PR to see the automation in action
5. Observe the validation results

## 📄 License

This is a demonstration project for internal POC testing.

## 🔗 Related Resources

- [uv Documentation](https://github.com/astral-sh/uv)
- [pytest Documentation](https://docs.pytest.org/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

---

**Made with ❤️ for PR Automation POC Testing**