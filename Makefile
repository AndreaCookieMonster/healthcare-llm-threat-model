.PHONY: linkcheck

linkcheck:
	@docker run --rm -v $(CURDIR):/repo -w /repo lycheeverse/lychee:latest --config .lychee.toml --verbose
	@if [ -d _site ]; then \
		docker run --rm -v $(CURDIR):/repo -w /repo lycheeverse/lychee:latest --config .lychee.toml --verbose /repo/_site/**/*.html; \
	else \
		echo "_site/ not found; skipping built-site link check"; \
	fi
