import streamlit as st

# Define mock product data with placeholder images
products = {
    1: {"name": "Hammer", "description": "A high-quality hammer suitable for all your construction needs.", "image_url": "https://via.placeholder.com/150"},
    2: {"name": "Screwdriver", "description": "Ergonomic screwdriver, perfect for all screw types.", "image_url": "https://via.placeholder.com/150"},
    3: {"name": "Wrench", "description": "Adjustable wrench with a comfortable grip.", "image_url": "https://via.placeholder.com/150"}
}

# Function to search for products


def search_products(query):
    return {pid: prod for pid, prod in products.items() if query.lower() in prod['name'].lower()}

# Main page function with product search and enhanced display


def main_page():
    st.title('Home Depot Shopping Platform')
    query = st.text_input('Search for products',
                          on_change=clear_product_selection)

    if query:
        results = search_products(query)
        if results:
            for product_id, product in results.items():
                col1, col2 = st.columns([1, 4])
                with col1:
                    st.image(product['image_url'], width=100)
                with col2:
                    st.subheader(product['name'])
                    if st.button('View', key=product_id):
                        st.session_state['product_id'] = product_id
                        st.session_state['navigation'] = 'Product Details'
                        st.experimental_rerun()
        else:
            st.warning(
                "No products found matching your search. Please try again with a different query.")

# Helper function to clear product selection when initiating a new search


def clear_product_selection():
    if 'product_id' in st.session_state:
        del st.session_state['product_id']

# Product details page function


def product_page(product_id):
    product = products[product_id]
    st.title(product['name'])
    st.image(product['image_url'], width=150)
    st.write(product['description'])
    # if st.button('Add to Cart'):
        # st.success('Product added to cart!')


# Initialize session state for navigation
if 'navigation' not in st.session_state:
    st.session_state['navigation'] = 'Home'

# Sidebar navigation setup
st.sidebar.title("Navigation")
st.sidebar.radio("Go to", ('Home', 'Product Details'),
                 index=0 if st.session_state['navigation'] == 'Home' else 1)

# Conditional rendering based on navigation state
if st.session_state['navigation'] == 'Home':
    main_page()
elif st.session_state['navigation'] == 'Product Details' and 'product_id' in st.session_state:
    product_page(st.session_state['product_id'])
else:
    st.session_state['navigation'] = 'Home'
    st.experimental_rerun()
