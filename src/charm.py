#!/usr/bin/env python3
# Copyright 2022 Unicorn
# See LICENSE file for licensing details.
#
# Learn more at: https://juju.is/docs/sdk

"""Charm the service.

Refer to the following post for a quick-start guide that will help you
develop a new k8s charm using the Operator Framework:

    https://discourse.charmhub.io/t/4208
"""

import logging

from ops.charm import CharmBase
from ops.framework import StoredState
from ops.main import main
from ops.model import ActiveStatus

logger = logging.getLogger(__name__)


class CharmHistoryOverheatCharm(CharmBase):
    """Charm the service."""

    _config_history = StoredState()

    def __init__(self, *args):
        super().__init__(*args)
        self.framework.observe(self.on.config_changed, self._on_config_changed)
        self._config_history.set_default(test_key=[])
        self.unit.status = ActiveStatus("unit is ready")

    def tack(self) -> None:
        """Tracking a specific key in config."""
        current_value = self.config.get("test-key")
        try:
            last_value = self._config_history.test_key[-1]
        except IndexError:
            last_value = None

        if last_value != current_value:
            self._config_history.test_key.append(current_value)

    def _on_config_changed(self, _):
        """Testing config changed handler."""
        if self.config["history"]:
            logger.info("tracking config history is enabled")
            self.tack()
            logger.info(f"tracking is done")


if __name__ == "__main__":
    main(CharmHistoryOverheatCharm)
