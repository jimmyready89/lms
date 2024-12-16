import PropTypes from 'prop-types';
import { Link, NavLink } from 'react-router-dom';
import { XMarkIcon } from '@heroicons/react/24/outline';
import {
    Button,
    IconButton,
    Typography,
} from '@material-tailwind/react';
import { useMaterialTailwindController, setOpenSidenav } from '../../context';

export function Sidenav({ brandName }) {
    const [controller, dispatch] = useMaterialTailwindController();
    const { sidenavType, openSidenav } = controller;
    const sidenavTypes = {
        dark: 'bg-gradient-to-br from-gray-800 to-gray-900',
        white: 'bg-white shadow-sm',
        transparent: 'bg-transparent',
    };

    return (
        <aside
            className={`${sidenavTypes[sidenavType]} ${
                openSidenav ? 'translate-x-0' : '-translate-x-80'
            } fixed inset-0 z-50 my-4 ml-4 h-[calc(100vh-32px)] w-72 rounded-xl transition-transform duration-300 xl:translate-x-0 border border-blue-gray-100`}
        >
            <div
                className="relative"
            >
                <Link to="/" className="py-6 px-8 text-center">
                    <Typography variant="h6" color={sidenavType === 'dark' ? 'white' : 'blue-gray'}>
                        {brandName}
                    </Typography>
                </Link>
                <IconButton
                    variant="text"
                    color="white"
                    size="sm"
                    ripple={false}
                    className="absolute right-0 top-0 grid rounded-br-none rounded-tl-none xl:hidden"
                    onClick={() => setOpenSidenav(dispatch, false)}
                >
                    <XMarkIcon strokeWidth={2.5} className="h-5 w-5 text-white" />
                </IconButton>
            </div>
            <div className="m-4">
                <ul className="mb-4 flex flex-col gap-1">
                    <li>
                        <NavLink to="/home">
                            <Button variant="text" color="white" className="flex items-center gap-4 px-4 capitalize" fullWidth>
                                <Typography color="inherit" className="font-medium capitalize" />
                            </Button>
                        </NavLink>
                    </li>
                </ul>
            </div>
        </aside>
    );
}

Sidenav.defaultProps = {
    brandName: 'Material Tailwind React',
};

Sidenav.propTypes = {
    brandName: PropTypes.string,
    routes: PropTypes.arrayOf(PropTypes.object).isRequired,
};

Sidenav.displayName = '/src/widgets/layout/sidnave.jsx';

export default Sidenav;
