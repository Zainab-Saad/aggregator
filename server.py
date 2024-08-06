from pathlib import Path
import pickle as pkl

import hydra
from hydra.core.hydra_config import HydraConfig
from omegaconf import DictConfig, OmegaConf
import flwr as fl

from src.utils import (
    evaluate_metrics_aggregation,
    config_func
)

@hydra.main(config_path="conf", config_name="base", version_base=None)
def main(cfg: DictConfig):
    print(OmegaConf.to_yaml(cfg))

    strategy = fl.server.strategy.FedXgbBagging(
        min_fit_clients=cfg.num_clients_per_round_fit,
        min_available_clients=cfg.num_clients,
        min_evaluate_clients=cfg.num_clients_per_round_eval,
        evaluate_metrics_aggregation_fn=evaluate_metrics_aggregation,
        on_evaluate_config_fn=config_func,
        on_fit_config_fn=config_func
    )

    history = fl.server.start_server(
        server_address="0.0.0.0:8080",
        config=fl.server.ServerConfig(cfg.num_rounds),
        strategy=strategy
    )

    save_path = HydraConfig.get().runtime.output_dir

    results_path = Path(save_path)/"results.pkl"

    results = {
        "history": history
    }

    with open(str(results_path), "wb") as h:
        pkl.dump(results, h, protocol=pkl.HIGHEST_PROTOCOL)

if __name__ == "__main__":
    main()