import React from 'react';
import TextField from '@material-ui/core/TextField';
import { FieldRenderProps } from 'react-final-form';

const MyTextField = <T extends {}>({ input, meta, ...rest }: FieldRenderProps<T, HTMLInputElement>) => {
    const handleOnChange = (event: React.ChangeEvent<HTMLInputElement>) => input.onChange(event.target.value);
    const { onChange, ...otherInput } = input;
    return (
        // @ts-ignore
        <TextField
            variant="standard"
            onChange={handleOnChange}
            error={!!meta.touched && !!meta.error}
            {...otherInput}
            {...rest}
        />
    );
};

export default MyTextField;
