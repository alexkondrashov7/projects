from xgboost import XGBClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import VotingClassifier
from catboost import CatBoostClassifier

random_state = 42

def fit_model(X_train_new, y_train):
    xgb = XGBClassifier(random_state = random_state, device = 'cuda',n_jobs = -1, reg_lambda  =0.5, reg_alpha = 1, n_estimators = 800, max_depth = 10, learning_rate = 0.01)
    ctb = CatBoostClassifier(random_state=random_state,devices='0',task_type = 'GPU',eval_metric='F1',thread_count=4,allow_writing_files=True,used_ram_limit='8gb',
                        learning_rate = 0.1,l2_leaf_reg = 0.001,iterations = 1000, depth = 5 )
    intervals_cols = selector.get_feature_names_out()
    transformer = ColumnTransformer(transformers=[
        ('scl',StandardScaler(),intervals_cols)],remainder='passthrough')
    knn = Pipeline(steps=[
        ('transformer',transformer),
        ('model',KNeighborsClassifier(n_jobs=-1,p =1, n_neighbors=14, metric = 'manhattan' ) )])

    xgb.fit(X_train_new, y_train)
    ctb.fit(X_train_new, y_train)
    knn.fit(X_train_new, y_train)

    voting_model = VotingClassifier(estimators=[('ctb',ctb),('xgb',xgb),('knn',knn)],voting='soft')

    voting_model.fit(X_train_new, y_train)

