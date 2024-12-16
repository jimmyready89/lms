import { Routes, Route, Navigate } from 'react-router-dom';
import { Sidenav } from '../widgets/layout';
import { Home } from '../pages/home';

function MainPage() {
    return (
        <div className="min-h-screen bg-blue-gray-50/50">
            <Sidenav brandName="LMS Offline" />
            <div className="p-4 xl:ml-80">
                <Routes>
                    <Route exact path="/home" element={<Home />} />
                    <Route path="*" element={<Navigate to="/home" replace />} />
                </Routes>
            </div>
        </div>
    );
}

export default MainPage;
