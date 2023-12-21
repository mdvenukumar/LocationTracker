import streamlit as st
import geocoder

def get_location():
    try:
        # Get location based on IP address (less accurate)
        location_ip = geocoder.ip('me')
        return location_ip

    except geocoder.GeocoderTimedOut as timeout_error:
        st.error(f"Timeout error occurred: {timeout_error}")
    except geocoder.GeocoderServiceError as service_error:
        st.error(f"Geocoder service error occurred: {service_error}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
    return None

def print_location(location, label):
    if location is not None and location.latlng:
        st.write(f"\n{label} Location:")
        st.write(f"Latitude: {location.latlng[0]}")
        st.write(f"Longitude: {location.latlng[1]}")
    else:
        st.warning(f"Failed to retrieve {label.lower()} location.")

def main():
    st.title("Location Information App")

    # Button to trigger location retrieval
    if st.button("Get Location"):
        # Get location when the button is clicked
        location_ip = get_location()
        print_location(location_ip, "IP")

if __name__ == "__main__":
    main()
