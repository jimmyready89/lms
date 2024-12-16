import { NavLink } from 'react-router-dom';

function ItemSideBar({ Icon, Name }) {
    return (
        <NavLink to="/home">
            <Button variant="text" color="white" className="flex items-center gap-4 px-4 capitalize" fullWidth>
                {Icon}
                <Typography color="inherit" className="font-medium capitalize">
                    {Name}
                </Typography>
            </Button>
        </NavLink>
    );
}

export default ItemSideBar;
