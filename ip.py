import streamlit as st
import geocoder

def get_location():
    try:
        # Get location based on IP address (less accurate)
        location_ip = geocoder.ip('me')
        st.write("Location based on IP address:")
        st.write("Latitude:", location_ip.latlng[0])
        st.write("Longitude:", location_ip.latlng[1])

        # Get location based on more accurate methods (requires internet connection)
        location_accurate = geocoder.ip('me', method='reverse')
        st.write("\nAccurate Location:")
        st.write("Latitude:", location_accurate.latlng[0])
        st.write("Longitude:", location_accurate.latlng[1])

        # Display map with the accurate location
        st.map([(location_accurate.latlng[0], location_accurate.latlng[1])])

    except Exception as e:
        st.write("An error occurred:", str(e))

if __name__ == "__main__":
    st.title("Location App")

    # Create a button to trigger the execution of get_location
    if st.button("Get Location"):
        get_location()

