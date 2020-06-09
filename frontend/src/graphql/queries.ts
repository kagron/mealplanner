import { gql } from 'apollo-boost';

const GET_USER = gql`
    {
        user {
            username
            firstName
            lastName
            email
        }
    }
`;

export { GET_USER };
