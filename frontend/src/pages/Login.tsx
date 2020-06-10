import React, { useEffect } from 'react';

// MUI
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import Link from '@material-ui/core/Link';
import Grid from '@material-ui/core/Grid';
import Box from '@material-ui/core/Box';
import LockOutlinedIcon from '@material-ui/icons/LockOutlined';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';

// Inputs
import MyTextField from '../components/inputs/MyTextField';

// React Final Form
import { Form, Field } from 'react-final-form';

// React Router
import { Link as RouterLink, RouteComponentProps } from 'react-router-dom';

// Apollo
import { useMutation } from '@apollo/react-hooks';
import { LOGIN } from '../graphql/mutations';

// Notistack
import { useSnackbar } from 'notistack';
import { CURRENT_USER, CURRENT_USER_INFO } from '../lib/constants';

type LoginFormValues = {
    email: string;
    password: string;
};

function Copyright() {
    return (
        <Typography variant="body2" color="textSecondary" align="center">
            {'Copyright © '}
            <Link color="inherit" to="/" component={RouterLink}>
                Meal Planner
            </Link>{' '}
            {new Date().getFullYear()}
            {'.'}
        </Typography>
    );
}

const useStyles = makeStyles((theme) => ({
    paper: {
        marginTop: theme.spacing(8),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    },
    avatar: {
        margin: theme.spacing(1),
        backgroundColor: theme.palette.secondary.main,
    },
    form: {
        width: '100%', // Fix IE 11 issue.
        marginTop: theme.spacing(1),
    },
    submit: {
        margin: theme.spacing(3, 0, 2),
    },
}));

const Login = (props: RouteComponentProps) => {
    const classes = useStyles();
    const { enqueueSnackbar } = useSnackbar();
    const [login, { loading, error, data }] = useMutation<TokenAuth, { username: string; password: string }>(LOGIN, {
        onCompleted: (data) => {
            if (data && data.tokenAuth && data.tokenAuth.token) {
                console.log(data.tokenAuth.token);
                // enqueueSnackbar('Successfully Logged in!', {
                //     variant: 'success',
                // });
                localStorage.setItem(CURRENT_USER, data.tokenAuth.token);
                localStorage.setItem(CURRENT_USER_INFO, JSON.stringify(data.tokenAuth));
                // window.location.pathname = '/';
                props.history.push('/');
            }
        },
        onError: (error) => {
            if (error) {
                console.error(error);
                enqueueSnackbar(error.message, {
                    variant: 'error',
                });
            }
        },
    });
    useEffect(() => {
        console.log(loading);
        console.log({ error, data });
    }, [loading]);

    const handleSubmit = (values: LoginFormValues) => {
        const { email, password } = values;
        login({ variables: { username: email, password } });
    };

    const validate = (values: LoginFormValues) => {
        const validateErrors = {} as any;
        if (!values.email) {
            validateErrors.email = 'Required';
        }
        if (!values.password) {
            validateErrors.password = 'Required';
        }
        return validateErrors;
    };

    return (
        <Container component="main" maxWidth="xs">
            <div className={classes.paper}>
                <Avatar className={classes.avatar}>
                    <LockOutlinedIcon />
                </Avatar>
                <Typography component="h1" variant="h5">
                    Sign in
                </Typography>
                <Form<LoginFormValues> onSubmit={handleSubmit} {...{ validate }}>
                    {({ handleSubmit, submitting }) => {
                        return (
                            <form className={classes.form} onSubmit={handleSubmit} noValidate>
                                <Field
                                    name="email"
                                    component={MyTextField}
                                    label="Email Address"
                                    fullWidth
                                    margin="normal"
                                    variant="outlined"
                                    autoComplete="email"
                                    autoFocus
                                />
                                <Field
                                    name="password"
                                    component={MyTextField}
                                    label="Password"
                                    fullWidth
                                    margin="normal"
                                    variant="outlined"
                                    type="password"
                                    autoComplete="current-password"
                                />
                                <Button
                                    type="submit"
                                    fullWidth
                                    disabled={submitting}
                                    variant="contained"
                                    color="primary"
                                    className={classes.submit}
                                >
                                    Sign In
                                </Button>
                                <Grid container>
                                    <Grid item xs>
                                        <Link to="/forgot-password" component={RouterLink} variant="body2">
                                            Forgot password?
                                        </Link>
                                    </Grid>
                                    <Grid item>
                                        <Link to="/register" component={RouterLink} variant="body2">
                                            {"Don't have an account? Sign Up"}
                                        </Link>
                                    </Grid>
                                </Grid>
                            </form>
                        );
                    }}
                </Form>
            </div>
            <Box mt={8}>
                <Copyright />
            </Box>
        </Container>
    );
};

export default Login;
