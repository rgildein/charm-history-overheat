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
from ops.main import main
from ops.model import ActiveStatus

logger = logging.getLogger(__name__)


class CharmHistoryOverheatCharm(CharmBase):
    """Charm the service."""

    def __init__(self, *args):
        super().__init__(*args)
        self.framework.observe(self.on.config_changed, self._on_config_changed)
        if self.model.config["history"]:
            self.framework.tacked(["test-key"])

        self.unit.status = ActiveStatus("unit is ready")

    def _on_config_changed(self, _):
        """Testing config changed handler."""
        logger.info("config-changed: test-key={}".format(self.config["test-key"]))


if __name__ == "__main__":
    main(CharmHistoryOverheatCharm)
