from ai.src.tuning.optuna_objective import objective
import optuna

study = optuna.create_study(direction="maximize")
study.optimize(objective, n_trials=20)

print("Best trial:")
print(study.best_trial)
