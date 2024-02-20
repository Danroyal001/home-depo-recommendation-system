import streamlit as st
import functools

# Carousel for related products


# @functools.lru_cache(maxsize=128)
def find_related_products(product):
    # 5 related products
    related_products_list = product['related_items'] if 'related_items' in product else [
    ]

    other_search_results = st.session_state['other_search_results'] if 'other_search_results' in st.session_state else [
    ]

    related_products_list = related_products_list + other_search_results

    # Insert a horizontal line divider
    st.markdown("---")

    st.write("Related Products:")

    print("related_products_list: ", related_products_list)
    print("other_search_results: ", other_search_results)

    if related_products_list:
        col1, col2, col3, col4, col5 = st.columns(5)

        cols = [col1, col2, col3, col4, col5]

        current_iteration_index = 0

        for related_product in related_products_list:
            with cols[current_iteration_index]:
                st.image(
                    related_product['product_image_url'], caption=related_product['product_name'], use_column_width=True)

                st.write(product['product_name'])

                if st.button('View', key=related_product['product_uid']):
                    st.session_state['product'] = related_product
                    st.session_state['other_search_results'] = other_search_results
                    st.switch_page("pages/2_🛒_Product_Page.py")

            if current_iteration_index == 4:
                break
            else:
                current_iteration_index += 1

    else:
        st.warning("Sorry, no related products found!!!")


if st.button('Return Home'):
    st.switch_page("1_🏡_Homepage.py")

if 'product' in st.session_state:
    product = st.session_state['product']

    st.title(product['product_name'])
    st.image(product['product_image_url'], width=150)
    st.markdown("*Reason for Recommendation*: " + product['reason_for_recommendaion'])
    st.markdown("*Relevance Score*: " + product['search_relevance_score'])
    st.markdown("*Product Description*: " + product['product_description'])

    # if st.button('Add to Cart'):
    #     st.success('Product added to cart!')

    find_related_products(product)

else:
    st.write("Return to the homepage and search for a product first!")
