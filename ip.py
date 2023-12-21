import streamlit as st
import geocoder
import pandas as pd

def get_location():
    location = geocoder.ip('me')
    return location.latlng

def main():
    st.title("Location Tracer App")

    if st.button("Trace Location"):
        location = get_location()
        if location:
            data = {'latitude': [location[0]], 'longitude': [location[1]]}
            df = pd.DataFrame(data)
            st.write("Location Information:")
            st.write(f"- Latitude: {location[0]}")
            st.write(f"- Longitude: {location[1]}")
            st.map(df, zoom=12)
        else:
            st.warning("Unable to retrieve location. Please try again.")

if __name__ == "__main__":
    main()
