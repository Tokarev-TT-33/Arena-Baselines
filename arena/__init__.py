from .arena import *
from .eval import *
from .vis import *
from .utils import prepare_path
from .rollout_worker import ArenaRolloutWorker

from ray.tune.registry import register_env

register_env(
    "Arena-Tennis-Sparse-2T1P-Discrete",
    lambda env_config: ArenaRllibEnv(
        "Arena-Tennis-Sparse-2T1P-Discrete",
        env_config=env_config,
    ))

register_env(
    "Arena-Blowblow-Sparse-2T2P-Discrete",
    lambda env_config: ArenaRllibEnv(
        "Arena-Blowblow-Sparse-2T2P-Discrete",
        env_config=env_config,
    ))
