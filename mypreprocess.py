from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, LabelEncoder
import category_encoders as ce 

from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer


def create_preprocessing():

    cat_columns =['StoreType', 'Assortment']
    num_columns = ['Customers', 'Competition_Since_X_months', 'CompetitionDistance']
    
# cols=['Promo', 'Promo2', 'PromoInterval', 'StateHoliday'],
    # Make pipelines for categorical and numerical features
    cat_pipeline = make_pipeline(ce.OneHotEncoder(handle_unknown="ignore"))
    num_pipeline = make_pipeline(SimpleImputer(strategy="mean"), StandardScaler())

    preprocessing = make_column_transformer(
        (cat_pipeline, cat_columns),
        (num_pipeline, num_columns),
        remainder='drop')

    return preprocessing

