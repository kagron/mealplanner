import React from 'react';

// React Router
import { RouteProps, Redirect, Route } from 'react-router';

// Apollo
import { gql } from 'apollo-boost';
import { useQuery } from '@apollo/react-hooks';
import { GET_USER } from '../graphql/queries';

// MUI
import CircularProgress from '@material-ui/core/CircularProgress';
import { Container, makeStyles } from '@material-ui/core';

// Notistack
import { useSnackbar } from 'notistack';

const useStyles = makeStyles((theme) => ({
    paper: {
        marginTop: theme.spacing(8),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    },
}));

const AuthenticatedRoute = (props: RouteProps) => {
    const classes = useStyles();
    const { loading, error, data } = useQuery<User>(GET_USER);
    const { enqueueSnackbar } = useSnackbar();
    if (error) {
        console.error(error);
        enqueueSnackbar(error.message);
    }
    return loading ? (
        <Container component="main" maxWidth="xs">
            <div className={classes.paper}>
                <CircularProgress />
            </div>
        </Container>
    ) : error ? (
        <div>Error!</div>
    ) : data && data.user ? (
        <Route {...props} />
    ) : (
        <Redirect to="/login" />
    );
};

export default AuthenticatedRoute;
