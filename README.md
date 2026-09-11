# OSS CI trust lab

A contributor forks this public repository and opens a PR upstream. Harness prepares approved test data, runs isolated tests against pinned base and PR head commits, and reports the result from a separate trusted stage.

The contributor does not need a Harness account. Pipeline YAML comes from upstream main and contains no pipeline-level name or identifier. The worker receives approved data, not the download credential.
