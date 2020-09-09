import streamlit as st

KITTENS_IMG = "https://images.unsplash.com/photo-1570018144715-43110363d70a?ixlib=rb-1.2.1&auto=format&fit=crop&w=1830&q=80"
KITTEN1_IMG = "https://images.unsplash.com/photo-1542404467-c68ef6f41a5d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2550&q=80"
KITTEN2_IMG = "https://images.unsplash.com/photo-1582081660251-54f4ddf7ec19?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2550&q=80"
KITTEN3_IMG = "https://images.unsplash.com/photo-1516750105099-4b8a83e217ee?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2550&q=80"


"Let's start with this image of kittens. It's great, but... those kittens are a bit crowded. Let's use `st.columns` to give those kittens some space."
st.image(KITTENS_IMG, use_column_width=True)

if st.button("Split to columns!"):
    with st.echo("below"):
        c1, c2, c3 = st.columns(3)
        c1.image(KITTEN1_IMG, use_column_width=True)
        c2.image(KITTEN2_IMG, use_column_width=True)
        c3.image(KITTEN3_IMG, use_column_width=True)
