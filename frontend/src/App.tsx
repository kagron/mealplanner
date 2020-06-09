import React from 'react';
import './App.css';

// React Router
import { Switch, Route, BrowserRouter as Router } from 'react-router-dom';

// Pages
import Login from './pages/Login';
import Register from './pages/Register';
import Dashboard from './pages/Dashboard';

// Apollo
import ApolloClient from 'apollo-boost';
import { ApolloProvider } from '@apollo/react-hooks';
import AuthenticatedRoute from './components/AuthenticatedRoute';

// Js Cookie
import Cookies from 'js-cookie';

// MUI
import { createMuiTheme, ThemeProvider } from '@material-ui/core';

// Notistack
import { SnackbarProvider } from 'notistack';

// Constants
import { CURRENT_USER } from './lib/constants';

const theme = createMuiTheme({
    palette: {
        type: 'light',
        primary: {
            main: '#2274A5', // light blue
        },
        secondary: {
            main: '#E7DFC6', // eggshell
        },
        background: {
            default: '#E9F1F7', // off white
            paper: '#E9F1F7', // off white
            // Black: '#131B23'
            // Brown: '#816C61'
        },
    },
});

const App: React.FC = () => {
    const csrfToken = Cookies.get('csrftoken');
    const currentUser = localStorage.getItem(CURRENT_USER);
    const client = new ApolloClient({
        headers: {
            // 'X-CSRFToken': csrfToken,
            ...(currentUser ? { Authorization: `JWT ${currentUser}` } : undefined),
        },
    });
    return (
        <ApolloProvider {...{ client }}>
            <ThemeProvider theme={theme}>
                <SnackbarProvider maxSnack={3}>
                    <Router>
                        <Switch>
                            <Route path="/login" component={Login} />
                            <Route path="/register" component={Register} />
                            <AuthenticatedRoute path="/" component={Dashboard} />
                        </Switch>
                    </Router>
                </SnackbarProvider>
            </ThemeProvider>
        </ApolloProvider>
    );
};

export default App;
