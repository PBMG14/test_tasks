from pyspark.sql import DataFrame

def get_products_with_categories(products_df: DataFrame,
                                 categories_df: DataFrame,
                                 product_category_links_df: DataFrame) -> DataFrame:
    result_df = (
        products_df
        .join(product_category_links_df, "product_id", "left")
        .join(categories_df, "category_id", "left")
        .select("product_name", "category_name")
        .distinct()
    )
    
    return result_df.orderBy("product_name", "category_name")
