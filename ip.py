import geocoder
import streamlit as st

def get_location():
    try:
        # Get location based on IP address (less accurate)
        location_ip = geocoder.ip('me')
        return location_ip.latlng
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None

def main():
    st.title("Location Coordinates App")
    
    # Button to trigger location retrieval
    if st.button("Get Location"):
        coordinates = get_location()
        
        # Display coordinates if available
        if coordinates:
            st.success("Coordinates Retrieved:")
            st.write(f"Latitude: {coordinates[0]}")
            st.write(f"Longitude: {coordinates[1]}")

if __name__ == "__main__":
    main()
