// Apollo
import { useQuery, useMutation } from '@apollo/react-hooks';

// Constants
import { CURRENT_USER, CURRENT_USER_INFO } from '../lib/constants';

// Moment
import moment from 'moment';

// Mutations
import { REFRESH } from './mutations';

const useAuthQuery: typeof useQuery = (...args) => {
    const currentUser = localStorage.getItem(CURRENT_USER);
    const preParseCurrentUserInfo = localStorage.getItem(CURRENT_USER_INFO);
    const currentUserInfo: TokenAuth['tokenAuth'] | null = preParseCurrentUserInfo
        ? JSON.parse(preParseCurrentUserInfo)
        : null;
    const now = moment().unix();
    const [refresh, { loading, error, data }] = useMutation<TokenAuth, { username: string; password: string }>(
        REFRESH,
        {
            onCompleted: (data) => {
                if (data && data.tokenAuth && data.tokenAuth.token) {
                    localStorage.setItem(CURRENT_USER, data.tokenAuth.token);
                    localStorage.setItem(CURRENT_USER_INFO, JSON.stringify(data.tokenAuth));
                    window.location.pathname = '/';
                }
            },
            onError: (error) => {
                if (error) {
                    console.error(error);
                }
            },
        }
    );

    if (
        !currentUser ||
        !currentUserInfo ||
        !currentUserInfo.payload ||
        !currentUserInfo.payload.exp ||
        now >= currentUserInfo.payload.exp
    ) {
        console.info('need to refresh');
        console.info('need to refresh');
        refresh();
    }
    return useQuery(...args);
};

export default useAuthQuery;
