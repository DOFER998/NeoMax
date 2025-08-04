PACKAGE := neomax

.PHONY: lint
lint:
	ruff check $(PACKAGE)

.PHONY: lint-fix
lint-fix:
	ruff check $(PACKAGE) --fix

.PHONY: format
format:
	ruff format $(PACKAGE)
