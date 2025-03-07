import streamlit as st

from libs import Catalog, Product


st.title("Product Catalog")

if "catalog" not in st.session_state:
    st.session_state.catalog = Catalog("My Catalog")

pages = st.sidebar.selectbox(
    "Menu", ["Add New Products", "Manage Products", "Available Products"]
)

if pages == "Add New Products":
    st.write("### Add New Products")
    name = st.text_input("Name")
    price = st.number_input("Price", value=10, step=1)
    stock = st.number_input("Stock", value=1, step=1)

    save_product = st.button("Save Product")

    if save_product:
        new_product = Product(name, price, stock)
        st.session_state.catalog.products.append(new_product)
        st.rerun()


elif pages == "Manage Products":
    st.write("### Manage Products")
    if not st.session_state.catalog.products:
        st.write("There no product yet")
    for index, product in enumerate(st.session_state.catalog.products, 1):
        st.write(f"{index}. **{product.name} - ${product.price} - {product.stock}**")

        col1, col2, col3 = st.columns([5, 1, 1])
        with col1:
            amount = st.number_input("Enter Amount", key=f"amount_{index}", step=1)
        with col2:
            if st.button("Increase stock", key=f"increase_{index}"):
                product.increase_stock(amount)
                st.rerun()
        with col3:
            if st.button("Decrease Stock", key=f"decrease_{index}"):
                product.decrease_stock(amount)
                st.rerun()

elif pages == "Available Products":
    st.write("### Available Products")
    available_products = st.session_state.catalog.get_available_products()
    if not available_products:
        st.write("No available products")
    for index, product in enumerate(available_products, 1):
        st.write(f"{index}. **{product.name} - ${product.price} - {product.stock}**")
