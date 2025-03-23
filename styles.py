import streamlit as st
def styles_css():
    st.markdown("""
            <style>
            

            [data-testid="stMarkdownContainer"] p {
            font-weight: bold;
                }
                
            div[data-testid="stAppViewBlockContainer"] {
                padding-left: 1rem;
                padding-right: 1rem;
                padding: 2.5rem 2rem 1rem;
            }
                
            [data-testid="stMainBlockContainer"] {
                padding: 2rem 2rem 0rem 2rem !important;  /* Adjust top, right, bottom, left padding */
            }
            # min-width: 400px !important;
            [data-testid="stSidebar"] {
                
                max-width: 400px !important;
            }
                    
            /* Hide Sidebar Navigation (if needed) */
            div[data-testid="stSidebarNav"] { display: none; }
            div[data-testid="stSidebarHeader"] > img, div[data-testid="collapsedControl"] > img {
                    height: 3.0rem;
                    width: auto;
                }
            /* Center Sidebar Header and Logo */
            div[data-testid="stSidebarHeader"], div[data-testid="collapsedControl"] {
                display: flex;
                align-items: center;
                justify-content: center;
            }

            
                    
            div[data-testid="stElementContainer"] {
                margin-top: -5px; /* Adjust this value to reduce top spacing */
                margin-bottom: -5px; /* Adjust this value to reduce bottom spacing */
                padding-top: 1px !important;
                padding-bottom: 2px !important;}

            div[data-testid="stMetric"] {
                background-color: white;
                border: 2px solid #ddd;
                padding: 10px;
                border-radius: 10px;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
                text-align: center;
                    }
            div[data-testid="stMetricValue"] {
            font-size: 18px !important;  /* Adjust the text size of the metric value */
            font-weight: bold;  /* Make it bold for emphasis */
            color: #333;  /* Darker color for better readability */
            }

            div[data-testid="stMetricLabel"] {
                font-size: 12px !important;  /* Adjust label size */
                color: #666;  /* Lighten the label text */
            }
            /* Basic Styling for Inputs & Buttons */
            [data-baseweb="tag"], [data-baseweb="select"],
            [data-testid="tooltipHoverTarget"], [data-testid="stDateInput-Input"],
            [data-testid="baseButton-secondary"] {
                background: white;
                color: black;
                padding: 2px;
                border: 1px solid #d3d3d3;
                border-radius: 10px;
            }

            /* Hover & Active Effects */
            [data-baseweb="tag"]:hover, [data-baseweb="select"]:hover,
            [data-testid="baseButton-secondary"]:hover {
                background: #f0f0f0;
            }

            [data-baseweb="tag"]:active, [data-baseweb="select"]:active,
            [data-testid="baseButton-secondary"]:active {
                background: #d32f2f;
                color: white;
                border: 1px solid #b71c1c;
            }

            /* DataFrame Styling */
            .dataframe { width: 100%; }
            .dataframe td, .dataframe th { text-align: center; vertical-align: middle; }
            .gdg-input {
                text-align: center !important;
                font-weight: bold !important;
            }
                    
                

            .container {
                            border: 1px solid black;
                            padding: 10px;
                            margin-bottom: 10px;
                            height: 380px; /* Set desired height */
                            width: auto; /* Set desired width */
                            overflow-y: scroll; /* Enable vertical scrolling */
                            overflow-x: auto; /* Enable horizontal scrolling if needed */
                        }
                    
            .container2 {
                            border: 1px solid black;
                            padding: 10px;
                            margin-bottom: 10px;
                            height: 100px; /* Set desired height */
                            width: auto; /* Set desired width */
                            overflow-y: scroll; /* Enable vertical scrolling */
                            overflow-x: auto; /* Enable horizontal scrolling if needed */
                        }
            </style>
        """, unsafe_allow_html=True)