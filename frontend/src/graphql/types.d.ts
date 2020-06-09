declare type User = {
    user: Partial<{
        username: string;
        firstName: string;
        lastName: string;
        email: string;
    }>;
};

declare type TimeOfDayEnum = 'BREAKFAST' | 'LUNCH' | 'DINNER';

declare type Meal = {
    created: Date;
    updated: Date;
    timeOfDay: TimeOfDayEnum;
};

declare type TokenAuth = {
    tokenAuth: Partial<{
        token: string;
        refreshExpiresIn: number;
        payload: Partial<{
            username: string;
            exp: number;
            origIat: number;
        }>;
    }>;
};
