import { gql } from 'apollo-boost';

const LOGIN = gql`
    mutation tokenAuth($username: String!, $password: String!) {
        tokenAuth(username: $username, password: $password) {
            token
            payload
            refreshExpiresIn
        }
    }
`;

const REFRESH = gql`
    mutation refreshToken($token: String!) {
        refreshToken(token: $token) {
            token
            payload
            refreshExpiresIn
        }
    }
`;

const REGISTER = gql`
    {
        user {
            username
            firstName
            lastName
            email
        }
    }
`;

export { LOGIN, REGISTER, REFRESH };
