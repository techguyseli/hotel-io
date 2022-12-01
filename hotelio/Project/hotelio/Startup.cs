using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(hotelio.Startup))]
namespace hotelio
{
    public partial class Startup
    {
        public void Configuration(IAppBuilder app)
        {
            ConfigureAuth(app);
        }
    }
}
