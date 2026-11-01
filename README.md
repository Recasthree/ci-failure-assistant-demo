[![GitHub Actions CI status](https://github.com/Recasthree/ci-failure-assistant-demo/actions/workflows/github_py_ci.yaml/badge.svg)](https://github.com/Recasthree/ci-failure-assistant-demo/actions/workflows/github_py_ci.yaml)

# Flask Demo App with GitHub Actions CI

This repository contains a small Flask app and pytest suite. The main branch is the passing baseline. The ci-demo-failure branch is an acceptance fixture for CI failure diagnosis.

## CI Failure Assistant Acceptance Branch

On ci-demo-failure, the GitHub Actions workflow runs pytest only. The test test_ci_demo_intentional_assertion_failure contains a deterministic failing assertion so a workflow_run.completed event and pytest failure log can be observed. This failure is intentional and isolated to the acceptance branch.

The workflow grants only contents: read. It does not modify repository files, create branches, or open pull requests.

## Local setup

1. Create and activate a virtual environment.
2. Install dependencies: python -m pip install flask==2.3.3 pytest==7.4.2.
3. Run tests with python -m pytest -q.

## License

[MIT License](LICENSE)
