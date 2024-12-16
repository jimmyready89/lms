import PropTypes from 'prop-types';
import {
    Card,
    CardBody,
    Typography,
} from '@material-tailwind/react';
import { Link } from 'react-router-dom';

export function CourseCard({
    ID, Title, Score,
}) {
    return (
        <Link to={`./course-detail/${ID}`}>
            <Card className="mx-3 mb-6 border border-blue-gray-100">
                <CardBody className="p-4">
                    <div className="px-4 pb-4">
                        <Typography variant="h6" color="blue-gray" className="mb-2">
                            {Title}
                        </Typography>
                        <Typography variant="small" className="font-normal text-blue-gray-500 text-left">
                            {Score ? `Schore : ${Score}/100` : ''}
                        </Typography>
                        <Typography variant="small" className="font-normal text-blue-gray-500 text-right">
                            {Score ? `Schore : ${Score}/100` : ''}
                        </Typography>
                    </div>
                </CardBody>
            </Card>
        </Link>
    );
}

CourseCard.propTypes = {
    ID: PropTypes.string.isRequired,
    Title: PropTypes.string.isRequired,
    Score: PropTypes.node.isRequired,
};

export default CourseCard;
