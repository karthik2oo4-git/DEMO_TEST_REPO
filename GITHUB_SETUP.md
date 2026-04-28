# GitHub Setup Guide for PR Validation

Complete step-by-step guide to enable PR validation on this repository.

## ✅ What's Already Done

- ✅ Repository pushed to GitHub
- ✅ Workflow file configured (`.github/workflows/pr-validation.yml`)
- ✅ Validation config created (`.github/pr-validation.yml`)
- ✅ `GITHUB_TOKEN` is automatically provided by GitHub Actions (no setup needed!)

## 🔧 Required Setup Steps

### Step 1: Enable GitHub Actions (if not already enabled)

1. Go to https://github.ibm.com/karthikbgpillai/DEMO_TEST_REPO/settings/actions
2. Under **Actions permissions**, ensure one of these is selected:
   - ✅ **Allow all actions and reusable workflows** (recommended for testing)
   - ✅ **Allow enterprise, and select non-enterprise, actions and reusable workflows**
3. Click **Save**

### Step 2: Configure Branch Protection Rules

This is **required** to make the validation enforce merge blocking.

1. Go to https://github.ibm.com/karthikbgpillai/DEMO_TEST_REPO/settings/branches
2. Click **Add branch protection rule**
3. Configure as follows:

   **Branch name pattern:**
   ```
   main
   ```

   **Protection settings:**
   - ✅ **Require status checks to pass before merging**
     - Click **Add** and search for: `intelligent-pr-validation`
     - Select it from the list
   - ✅ **Require branches to be up to date before merging** (optional but recommended)
   - ✅ **Require linear history** (optional)
   - ✅ **Do not allow bypassing the above settings** (recommended)

4. Click **Create** or **Save changes**

### Step 3: Verify Workflow Permissions

1. Go to https://github.ibm.com/karthikbgpillai/DEMO_TEST_REPO/settings/actions
2. Scroll to **Workflow permissions**
3. Ensure these settings:
   - ✅ **Read and write permissions** (allows the bot to comment and set status)
   - ✅ **Allow GitHub Actions to create and approve pull requests** (optional)
4. Click **Save**

## 🧪 Testing the Setup

### Create a Test PR

1. **Create a test branch:**
   ```bash
   git checkout -b test/validation-check
   ```

2. **Make a simple change:**
   ```bash
   echo "# Test change" >> README.md
   git add README.md
   git commit -m "Test: Verify PR validation workflow"
   git push -u origin test/validation-check
   ```

3. **Open a Pull Request:**
   - Go to https://github.ibm.com/karthikbgpillai/DEMO_TEST_REPO/pulls
   - Click **New pull request**
   - Base: `main` ← Compare: `test/validation-check`
   - Click **Create pull request**

4. **Observe the validation:**
   - Go to the **Checks** tab on your PR
   - You should see `PR Unit Test Validation` running
   - Wait for it to complete

### Expected Results

**If everything is configured correctly:**

✅ **Checks tab shows:**
- Workflow: `PR Validation Demo`
- Job: `PR Unit Test Validation`
- Status: Green checkmark (if tests pass)

✅ **PR page shows:**
- Commit status: `intelligent-pr-validation` ✓
- Bot comment with validation summary
- Label: `ready-for-review` (if tests passed)

✅ **Merge button:**
- Enabled if all checks pass
- Blocked if any check fails

## 🔍 Troubleshooting

### Issue: Workflow doesn't run

**Check:**
1. GitHub Actions is enabled in repository settings
2. Workflow file exists at `.github/workflows/pr-validation.yml`
3. PR is not from a fork (forks have restricted permissions)

**Solution:**
- Go to Actions tab: https://github.ibm.com/karthikbgpillai/DEMO_TEST_REPO/actions
- Check if workflow appears in the list
- Click on it to see any error messages

### Issue: "Action not found" error

**Error message:**
```
Error: karthikbgpillai/POC_PR_AUTOMATION@main not found
```

**Solution:**
1. Verify the action repository exists: https://github.ibm.com/karthikbgpillai/POC_PR_AUTOMATION
2. Ensure you have access to that repository
3. Check if the action is published correctly

### Issue: Permission denied errors

**Error message:**
```
Error: Resource not accessible by integration
```

**Solution:**
1. Go to Settings → Actions → Workflow permissions
2. Select **Read and write permissions**
3. Save and re-run the workflow

### Issue: Status check not appearing in branch protection

**Solution:**
1. The status check name must match exactly: `intelligent-pr-validation`
2. The check must run at least once before it appears in the list
3. Create a test PR first, then add the branch protection rule

### Issue: Tests fail but merge is still allowed

**Solution:**
- Branch protection is not configured correctly
- Go to Settings → Branches
- Ensure `intelligent-pr-validation` is in the required status checks list
- Ensure "Require status checks to pass before merging" is checked

## 📊 What Happens in the Workflow

1. **Trigger:** PR opened/synchronized/reopened/ready_for_review
2. **Checkout:** PR head commit checked out with full history
3. **Merge:** Latest base branch merged into PR head in CI
4. **Setup:** 
   - `uv venv` creates isolated environment
   - `uv pip install -e .` installs project + dependencies
5. **Test:** `uv run pytest -q --maxfail=1` runs tests
6. **Results:**
   - Success → Green status, `ready-for-review` label, merge allowed
   - Failure → Red status, `test-failed` label, merge blocked
   - Merge conflict → Red status, `merge-conflict` label, merge blocked

## 🎯 Success Criteria

You'll know everything is working when:

1. ✅ PR triggers the workflow automatically
2. ✅ Workflow runs and completes (green or red)
3. ✅ Bot posts a comment on the PR
4. ✅ Commit status appears: `intelligent-pr-validation`
5. ✅ Labels are applied based on result
6. ✅ Merge button respects the check result

## 📝 No Secrets Required!

Unlike some CI systems, this setup **does not require** you to configure:
- ❌ `GITHUB_TOKEN` (automatically provided)
- ❌ `LANGGRAPH_SERVICE_URL` (removed in GitHub-native architecture)
- ❌ `LANGGRAPH_SERVICE_TOKEN` (removed in GitHub-native architecture)

The workflow uses only the built-in `GITHUB_TOKEN` that GitHub Actions provides automatically.

## 🔗 Quick Links

- **Repository:** https://github.ibm.com/karthikbgpillai/DEMO_TEST_REPO
- **Actions:** https://github.ibm.com/karthikbgpillai/DEMO_TEST_REPO/actions
- **Settings:** https://github.ibm.com/karthikbgpillai/DEMO_TEST_REPO/settings
- **Branch Protection:** https://github.ibm.com/karthikbgpillai/DEMO_TEST_REPO/settings/branches
- **Pull Requests:** https://github.ibm.com/karthikbgpillai/DEMO_TEST_REPO/pulls

## 🚀 Next Steps

1. ✅ Enable GitHub Actions (if needed)
2. ✅ Configure branch protection for `main`
3. ✅ Set workflow permissions to read/write
4. ✅ Create a test PR
5. ✅ Verify the workflow runs
6. ✅ Check that merge blocking works

That's it! No tokens or secrets to configure. 🎉