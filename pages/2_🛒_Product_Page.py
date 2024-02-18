import streamlit as st


def find_related_products(product, other_results=[]):
    # 5 related products
    related_products_list = product['related_items'] if 'related_items' in product else [
    ]

    if related_products_list:
        st.write("Related Products")
        col1, col2, col3, col4, col5 = st.columns(len(related_products_list))
        for related_product in related_products_list:
            # with col:
            st.image(
                related_product['product_image_url'], caption=related_product['name'], use_column_width=True)
            st.write(product['name'])
            if st.button('View', key=generate_uid()):
                st.switch_page("pages/2_🛒_Product_Page.py")


if st.button('Return Home'):
    st.switch_page("1_🏡_Homepage.py")

if 'product' in st.session_state:
    st.session_state['navigation'] = 'Home'
    st.experimental_rerun()

    st.title(product['product_name'])
    st.image(product['product_image_url'], width=150)
    st.write(product['product_description'])

    # if st.button('Add to Cart'):
    #     st.success('Product added to cart!')

    # find_related_products(product)

else:
    st.write("Return to the homepage and search for a product first!")
